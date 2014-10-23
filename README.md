xmarks2html
===========

A very simple script to transform xmarks .json file to html file


## Usage


```
python main.py bookmarks.json >index.html
```

## Motivation

You can use a private server to store your bookmarks of Xmarks service. Mere info: https://helpdesk.xmarks.com/bookmark-manager-basics/byos/

The bookmars are stored in a json format file. This little script transform the file into a html, using a template. You can execute it periodically to have a browsable copy of your bookmarks.

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

```
python xmarks2html.py
```

## Requirements

Testing under Python 2.7


## License

MIT
