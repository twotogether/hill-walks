# Hill Walks Tracker

A collection of hill walks organized by region with an interactive map showing all climbed hills.

## Structure

```
docs/
├── index.md                 # Main page
├── map.md                   # Interactive map (with Leaflet)
├── region-metadata.json     # Centralized metadata for all hills
└── regions/
    ├── index.md
    ├── east-lothian.md
    └── east-lothian/
        ├── images/          # Photos for East Lothian hills
        ├── north-berwick-law.md
        └── eildon-mid-hill.md
```

## Adding a New Hill

1. **Create a new markdown file** in the region subfolder:
   ```
   docs/regions/[region-name]/[hill-name].md
   ```

2. **Add metadata section** (visible on the page):
   ```markdown
   # Hill Name

   ## Details

   | Field | Value |
   |-------|-------|
   | **Coordinates** | 56.0588, -2.1384 |
   | **Hill Type** | Volcanic cone |
   | **Difficulty** | Easy |
   | **Elevation** | 187 m |
   | **Region** | East Lothian |

   ## Description
   ...

   ## Photos
   ![](../[region-name]/images/[image-name].jpg)
   ```

3. **Update `region-metadata.json`** with the new hill entry:
   ```json
   {
     "name": "Hill Name",
     "region": "Region",
     "latitude": 56.0588,
     "longitude": -2.1384,
     "elevation": 187,
     "difficulty": "Easy",
     "type": "Volcanic cone",
     "url": "regions/[region-name]/[hill-name].html"
   }
   ```

4. **Add to region index** in `docs/regions/[region-name].md`:
   ```markdown
   ```{toctree}

   [region-name]/[hill-name]
   ```
   ```

5. **Add photos** to the region's images folder:
   ```
   docs/regions/[region-name]/images/[image-name].jpg
   ```

## Building Locally

```bash
pip install -r requirements.txt
cd docs
sphinx-build -b html . ../_build/html
```

Then open `_build/html/index.html` in your browser.

## Deployment

Push to `main` branch — GitHub Actions automatically builds and deploys to GitHub Pages.

## Metadata Fields

- **Coordinates**: Latitude and longitude (used for map)
- **Hill Type**: e.g., "Volcanic cone", "Moorland", "Rocky peak"
- **Difficulty**: Easy, Medium, Hard
- **Elevation**: Height in meters

## Customization

Theme settings are in `docs/conf.py` — edit `html_theme_options` to customize the Furo theme.