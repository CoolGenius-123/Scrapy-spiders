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
        if 'all' not in gallery_link.split('/'):

            # finding the username as well
            username = gallery_link.partition('https://www.deviantart.com/')[2].partition('/gallery')[0]

            # extract the folderid from the gallery link
            folderid = re.findall(r'\d+', gallery_link)[-1]

            # using the base link to create the final link
            base_link = "https://www.deviantart.com/_puppy/dashared/gallection/contents?username=THE-HYPNOMAN&type=gallery&offset=0&limit=24&folderid=83189663&csrf_token=oV4S-PrtElXSH-ka.sbvhr3.4uUqvKS7AjapCjy8vV6RXzIbG0YqMjrJmWyrcK4h1X0&da_minor_version=20230710"


            final_link = re.sub(r'folderid=\d+', f'folderid={folderid}', base_link)

            final_link = final_link.replace('THE-HYPNOMAN', username)
        else:
            base_api = "https://www.deviantart.com/_puppy/dashared/gallection/contents?username=dollmistress&type=gallery&offset=72&limit=24&all_folder=true&csrf_token=oV4S-PrtElXSH-ka.sbvhr3.4uUqvKS7AjapCjy8vV6RXzIbG0YqMjrJmWyrcK4h1X0&da_minor_version=20230710"

            username = gallery_link.partition('https://www.deviantart.com/')[2].partition('/gallery')[0]

            final_link = base_api.replace('dollmistress', username)

        # Call the spider using subprocess
        sp.run(['scrapy', 'crawl', 'images', '-a', 'start_url='+final_link, '-o', 'output.json'])

        # Read the output file
        with open('output.json', 'r') as f:
            data = json.load(f)

        # Zip and Download the images folder
        shutil.make_archive('images', 'zip', 'images')

        # check if the images.zip exists
        if os.path.exists('images.zip'):
            st.write('Images Downloaded Successfully')

            with open('images.zip', 'rb') as f:
                btn = st.download_button(label='Download Images', data=f.read(), file_name='deviantart.zip', mime='application/zip')
        
        else:
            st.write('Images not downloaded')

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
        st.write('Refresh Page Please enter a gallery link')
else:
    gallery_link = None
    username = st.sidebar.text_input('Username')
    st.sidebar.text('Artist Username')
    if username:

        base_api = 'https://www.deviantart.com/_puppy/dashared/gallection/contents?username=dollmistress&type=gallery&offset=72&limit=24&all_folder=true&csrf_token=oV4S-PrtElXSH-ka.sbvhr3.4uUqvKS7AjapCjy8vV6RXzIbG0YqMjrJmWyrcK4h1X0&da_minor_version=20230710'

        final_link = base_api.replace('dollmistress', username)

        # Call the spider using subprocess
        sp.run(['scrapy', 'crawl', 'images', '-a', 'start_url='+final_link, '-o', 'output.json'])

        # Read the output file
        with open('output.json', 'r') as f:
            data = json.load(f)

        # Zip and Download the images folder
        shutil.make_archive('images', 'zip', 'images')

        # check if the images.zip exists
        if os.path.exists('images.zip'):
            st.write('Images Downloaded Successfully')

            with open('images.zip', 'rb') as f:
                btn = st.download_button(label='Download Images', data=f.read(), file_name='deviantart.zip', mime='application/zip')
        
        else:
            st.write('Images not downloaded')

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
        st.write('Refresh Page Please enter a Username')
    




