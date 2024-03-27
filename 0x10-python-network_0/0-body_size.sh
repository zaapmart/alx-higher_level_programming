#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided as an argument
url=$1

# Use curl to send a request to the URL and get the body size of the response
body_size=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the body size in bytes
echo "$body_size"

