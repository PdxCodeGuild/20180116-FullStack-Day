# music-share

## overview
General music sharing / recommendation / blog using the Discogs and Bandcamp API.

Users can search index of previously shared artists / media or signup to submit a record / artist / label for recommendation. Visitors and users can signup for email notifications if content or reviews have been added. As a user, you can save info to collections or wishlist to DB.

Once band / genre / label is searched, site will return data with name(s), basic bio, discography and related artists. 

Basic web-scraping could be used to track info posted in the past 6 months including new releases, reissues, tour and / or other info if available. Maybe import streamable content via bandcamp if available.

Continue browsing or logout.


## Database Models

- Blog post
    - foriegn key one-to-many / many-to-one to Label
- Artist
    - name
    - many-to-one to Label (nullable)
- Album
    - name
    - many-to-many with Artist
    - discogs album ID
- Label
    - name
    - many-to-many with Label
- UserFavorite
    - many to many with users
    - name



## Pages

- Regular music blog / site where visitors can browse eclectic content that has been previously entered. While reading an entry about a certain artist / release, bandcamp will load streamable content if available but Discogs API will always load at the bottom of the review / writeup.

- If a visitor wants to contribute or 'like' or add to a wish-list, there's login/sign-in screen to be granted writing / saving privileges.

- There will also be a logout screen.


## Features

- Users
    - add artist / label / album to favorites
    - write a blog post
    - search artist / label / album
    
- Visitors
    - browse previously shared artists
    - stream content from bandcamp
    - search Discogs API for artist / label / album
    





