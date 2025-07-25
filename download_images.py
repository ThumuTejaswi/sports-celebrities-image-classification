from bing_image_downloader import downloader

celebrities = [
    "ms dhoni", "sachin tendulkar",
    "cristiano ronaldo", "pv sindhu",
    "sunil chhetri","virat Kohli",
    "rohit sharma","pt usha","smriti mandhana"
]

for celeb in celebrities:
    folder_name = celeb.lower().replace(" ", "_")
    downloader.download(
        celeb,
        limit=40,
        output_dir="dataset",
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )