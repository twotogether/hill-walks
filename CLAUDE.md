# Hill Walks Tracker - Project Documentation

## Overview
A Sphinx-based documentation site for hill walks organized by region with an interactive Leaflet map showing all climbed hills.

## Project Structure

```
docs/
├── conf.py                      # Sphinx configuration
├── index.md                     # Main page
├── map.md                       # Interactive map (Leaflet.js + OpenStreetMap)
├── region-metadata.json         # Centralized hill metadata for map
├── .nojekyll                    # Disables Jekyll on GitHub Pages
└── regions/
    ├── index.md
    ├── [region-name].md         # Region page with toctree
    └── [region-name]/
        ├── [hill-name].md       # Hill walk page with metadata table + description
        └── images/              # Photos for that region
```

## Key Technologies
- **Sphinx**: Static site generator
- **Furo Theme**: Modern documentation theme with sidebar navigation
- **MyST Parser**: Parse Markdown with Sphinx extensions
- **Leaflet.js**: Interactive mapping library
- **OpenStreetMap**: Free map tiles
- **GitHub Actions**: CI/CD for building and deploying to GitHub Pages

## How It Works

1. **Hill data stored in two places**:
   - `region-metadata.json`: Single source of truth for map markers (coordinates, metadata)
   - Individual `.md` files: Rich narrative content (description, photos, route details)

2. **Map functionality**:
   - `map.md` fetches `region-metadata.json`
   - Leaflet renders green markers for each hill
   - Clicking a marker shows popup with details and link to full page

3. **Site navigation**:
   - Sidebar auto-generated from `toctree` directives in markdown files
   - Region pages group related hills
   - Main page lists all regions and links to map

## Adding Content

### New Hill
1. Create `docs/regions/[region]/[hill-name].md`
2. Add metadata table (visible on rendered page)
3. Add description, route, photos sections
4. Create `docs/regions/[region]/images/` folder for photos
5. Update `docs/region-metadata.json` with coordinates and metadata
6. Add entry to `docs/regions/[region].md` toctree

### New Region
1. Create `docs/regions/[region-name].md`
2. Create `docs/regions/[region-name]/` folder
3. Create `docs/regions/[region-name]/images/` folder
4. Add region to `docs/index.md` toctree and region list
5. Add region to `docs/regions/index.md` toctree

## Metadata Schema (region-metadata.json)

```json
{
  "hills": [
    {
      "name": "Hill Name",
      "region": "Region Name",
      "latitude": 55.5,
      "longitude": -2.0,
      "elevation": 500,
      "difficulty": "Easy|Medium|Hard",
      "type": "Hill type description",
      "url": "regions/region-name/hill-name.html"
    }
  ]
}
```

## Markdown Page Format

```markdown
# Hill Name

## Details

| Field | Value |
|-------|-------|
| **Coordinates** | 55.5, -2.0 |
| **Hill Type** | Volcanic cone |
| **Difficulty** | Medium |
| **Elevation** | 500 m |
| **Region** | Region Name |

## Description
Narrative description...

## Route
Route details...

## Photos
![](../region-name/images/photo.jpg)
*Caption*
```

## Building & Deployment

### Local Development
```bash
pip install -r requirements.txt
cd docs
sphinx-build -b html . ../_build/html
open ../_build/html/index.html
```

### GitHub Pages
- Push to `main` branch
- GitHub Actions builds with `sphinx-build`
- Deploys to GitHub Pages automatically
- URL: `https://[username].github.io/hill-walks/`

## Theme Customization

Edit `docs/conf.py`:
- `html_theme_options`: Furo theme settings
- `extensions`: Add Sphinx extensions
- `html_static_path`: Static assets

## Notes

- Metadata must be kept in sync between markdown pages and `region-metadata.json`
- Image paths are relative to the markdown file location
- URLs in `region-metadata.json` should point to the compiled HTML output paths
- Green marker icon sourced from Leaflet Color Markers GitHub repo
