# Image to Sketch Converter

A Python-based application that converts a ReadMe file (in `.md` or `.txt` format) into an image representation. The converter renders the content of the ReadMe file into a sketch-like image, ideal for showcasing textual information or visualizing content in a more creative format.

## Features

- **Markdown and Plain Text Support**: The converter supports `.md` and `.txt` file formats for conversion.
- **Image Generation**: Converts the content of ReadMe files into an image with a simple sketch-style layout.
- **Flask Backend**: Built using the Flask web framework, allowing users to upload their ReadMe files through a simple web interface.
- **Customizable Font and Style**: Modify font style, size, and background to suit your project requirements.

## Prerequisites

- **Python 3.7+**
- **Required Libraries**:
  - Flask
  - Pillow (PIL Fork)
  - markdown2

You can install the required libraries using `pip`:

```bash
pip install Flask Pillow markdown2
