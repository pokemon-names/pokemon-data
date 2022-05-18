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
    pip install yq --ignore-installed PyYAML

### JSON processing

    cat original/Bulbapedia-Gen-I-Sample.xml | xq '.' > processed/bulbapedia_gen_i_sample.json
    cat processed/bulbapedia_gen_i_sample.json | jq '.mediawiki.page | .[] | { id: .id, name: .title, origin: .revision.text."#text" }' > processed/processed/bulbapedia_gen_i_sample_slightly_simpler.json

### Text processing

    ...

