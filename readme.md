# RL LAB WEBSITE

## requirement
```
Jekyll 4.3.2
addressable-2.8.4
rouge-4.1.2
sass-embedded-1.64.1
```

## How to run
```shell
bundle exec jekyll serve # serve the page

bundle exec jekyll build # build the page
```

## Configuration
edit the json file in ``/_data/*.json``
### special description

```json5
// object in news.json
{
  "title": "",
  "desc": "",
  "date": "2023-09-21",
  // get icons from https://fonts.google.com/icons
  // Optional, default: "event"
  "google_icon": "check_circle_outline",
  // Optional, only takes effect when google_icon is null
  "icon": "url",
  // Optional, inverts the color of the image,
  // only takes effect when the icon is not null
  "invert": "boolean"
}
```

### About deploy site

git clone git@github.com:TJU-DRL-LAB/rl.beiyang.ren.git --depth=1 --filter=tree:_site/


