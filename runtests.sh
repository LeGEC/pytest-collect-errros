#!/bin/bash

echo "# tests run from command line, using pytest:"
echo "\$ pytest"
pytest
echo ""
echo "\$ pytest --continue-on-collection-errors"
pytest --continue-on-collection-errors
