import streamlit as st
import os
import re
import subprocess as sp
import json
import shutil

# columns matcher
values = {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5,
    '5': 1,
    '6': 2,
    '7': 3,
    '8': 4,
    '9': 5
}

# Title of the app
st.title('DeviantArt Downloader')

# remove output.jsom if it exists
if os.path.exists('output.json'):
    os.remove('output.json')

# remove images folder if it exists
if os.path.exists('images'):
    shutil.rmtree('images')

# remove images.zip if it exists
if os.path.exists('images.zip'):
    os.remove('images.zip')

# Sidebar
st.sidebar.title('Settings')
option = st.sidebar.radio('Choose an option', ['Gallery Link', 'Username'])

if option == 'Gallery Link':
    gallery_link = st.sidebar.text_input('Gallery Link')
    st.sidebar.text('Gallery Link')
    if gallery_link:
        gallery_link = gallery_link.split('/')
        if 'all' not in gallery_link:
            folderid = gallery_link[-2]

            base_link = "https://www.deviantart.com/_puppy/dashared/gallection/contents?username=THE-HYPNOMAN&type=gallery&offset=24&limit=24&folderid=38892697&csrf_token=ktfpqfMNl06v6onF.s9s404.8QK-yF6Hec8YoEO_hhHGhmtIOVgGYkcDPsq7KtrRpnU&da_minor_version=20230710"

            final_link = re.sub(r'folderid=\d+', f'folderid={folderid}', base_link)

            final_link = final_link.replace('THE-HYPNOMAN', gallery_link[-4])
        else:
            base_api = 'https://www.deviantart.com/_puppy/dashared/gallection/contents?username=dollmistress&type=gallery&offset=24&limit=24&all_folder=true&csrf_token=coqpp0Qy8ZBqUOWm.s8jlmm.0HhmNcG2KruMNYdSOxrUMRgewlTeemYivtHMEpGK6tM&da_minor_version=20230710'

            username = gallery_link[-4]

            final_link = base_api.replace('dollmistress', username)

        # Call the spider using subprocess
        sp.run(['scrapy', 'crawl', 'images', '-a', 'start_url='+final_link, '-o', 'output.json'])

        # Read the output file
        with open('output.json', 'r') as f:
            data = json.load(f)

        # Zip and Download the images folder
        shutil.make_archive('images', 'zip', 'images')

        # Display the download link
        st.markdown(f'[Download Images](./images.zip)')

        col1, col2, col3, col4, col5 = st.columns(5)
        count = 0
        # display the images from output along with the title
        for image in data:

            column_number = values[str(count)[-1]]

            if column_number == 1:
                with col1:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')

            elif column_number == 2:
                with col2:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')

            elif column_number == 3:
                with col3:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')

            elif column_number == 4:
                with col4:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
                    
            else:
                with col5:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            count += 1
            

        # Remove the output file
        os.remove('output.json')
    else:
        st.write('Please Enter a Link of The Gallery')
else:
    gallery_link = None
    username = st.sidebar.text_input('Username')
    st.sidebar.text('Artist Username')
    if username:
        base_api = 'https://www.deviantart.com/_puppy/dashared/gallection/contents?username=dollmistress&type=gallery&offset=24&limit=24&all_folder=true&csrf_token=coqpp0Qy8ZBqUOWm.s8jlmm.0HhmNcG2KruMNYdSOxrUMRgewlTeemYivtHMEpGK6tM&da_minor_version=20230710'

        final_link = base_api.replace('dollmistress', username)

        # Call the spider using subprocess
        sp.run(['scrapy', 'crawl', 'images', '-a', 'start_url='+final_link, '-o', 'output.json'])

        # Read the output file
        with open('output.json', 'r') as f:
            data = json.load(f)

        # Zip and Download the images folder
        shutil.make_archive('images', 'zip', 'images')

        # Display the download link
        st.markdown(f'[Download Images](./images.zip)')

        col1, col2, col3, col4, col5 = st.columns(5)
        count = 0
        # display the images from output along with the title
        for image in data:
            column_number = values[str(count)[-1]]
            if column_number == 1:
                with col1:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            elif column_number == 2:
                with col2:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            elif column_number == 3:
                with col3:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            elif column_number == 4:
                with col4:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            else:
                with col5:
                    st.image(image['image_url'], caption=image['image_name'], width=40, use_column_width='always')
            count += 1
            

        # Remove the output file
        os.remove('output.json')
    else:
        st.write('Please Enter A Username of The Deviant Artist It will Download All the Images of The Deviant Artist')
    




