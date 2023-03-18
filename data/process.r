# a short script to parse the wwp data down to just journal entries.
# we also limited the number of columns provided.
library(tidyverse)
dat <- read_csv('/Users/hathawayj/Downloads/2022-12-12-wwp-pages-export.csv')

journal <- dat |>
    filter(str_detect(`Parent Name`, "[Jj]ournal")) |>
    filter(str_detect(`Parent Name`, "Leaves", negate = TRUE)) |>
    count(`Parent Name`)

out <- dat |>
    filter(`Parent Name` %in% pull(journal,`Parent Name`)) |>
    rename_all(str_to_lower) |>
    rename_all(~str_replace_all(., " ", "_")) |>
    select(internal_id, parent_name, name,
        original_transcript, text_only_transcript, website_url)

write_csv(out, "data/journals.csv")
