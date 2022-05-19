## Source data for etymology pokedex

## 1. original

Original data is downloaded from the internet and stored here unmodified.

- Chrome "Save as HTML only"
- Chrome "Save as single file" -- this embeds all the style and images
- Wikimedia Export as XML -- for all wikimedia-based sites, for example Bulbapedia

## 2. processed

- HTML-only files have been reduced to just the headers and <table> tags.
- Wikimedia XML has been transformed to JSON, for ease of processing.

### XML to JSON

    python -m venv test1-env # optional
    source test1-env/bin/activate # optional
    pip install yq --ignore-installed PyYAML # yq package includes xq command

    cat data/original/Bulbapedia-Gen-I-Sample.xml | xq '.' > data/processed/bulbapedia_gen_i_sample.json

### JSON processing

Extract all relevant fields

    cat data/processed/bulbapedia_gen_i_sample.json | jq -r '.mediawiki.page | .[] | { id: .id, name: .title, content: .revision.text."#text" }' > data/processed/bulbapedia_gen_i_sample_reduced.json

Extract wikitext content

    cat data/processed/bulbapedia_gen_i_sample_reduced.json | jq -r '.content' > data/processed/bulbapedia_gen_i_sample_content.txt

### Wikitext processing

    See `scripts/parse_wikitext.py` which uses [wikitextparser](https://github.com/5j9/wikitextparser)

