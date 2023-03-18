# Data files

The `journals.csv` contains all the journal entries currently transcribed from Wilford Woodruff's journals. It has the following columns.

- `internal_id`: An id used by the papers project.
- `parent_name`: The name of the journal.
- `name`: The page number in `page_0000` format.
- `original_transcript`: The html formatted text from the journal page.
- `text_only_transcript`: The ascii text from the journal page.
- `website_url`: The url to the journal website.

The `lds-scriptures.csv` contains all four standard works of The Church of Jesus Christ of Latter-day Saints. It contains the following columns - `volume_id`, `book_id`, `chapter_id`, `verse_id`, `volume_title`, `book_title`, `volume_long_title`, `book_long_title`, `volume_subtitle`, `book_subtitle`, `volume_short_title`, `book_short_title`, `volume_lds_url`, `book_lds_url`, `chapter_number`, `verse_number`, `scripture_text`, `verse_title`, `verse_short_title`