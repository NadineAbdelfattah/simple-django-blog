from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "POOH",
        "date": date(2021, 6, 16),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec porta ligula. Quisque sem nisi, scelerisque sit amet pellentesque non,",
        "content": """
            Duis elementum lacus eu sapien ornare, id pharetra mi dignissim.
            Praesent nec eros commodo lacus dignissim eleifend non nec eros.
            Nulla vitae ante id ligula convallis viverra. 
            Curabitur eleifend pretium enim, eget porta sapien mollis et.
            Aliquam sagittis mi neque, ac venenatis enim pretium et.
            Aliquam quis blandit mauris, et ullamcorper nibh. 
            Vivamus laoreet metus eu nisi sollicitudin accumsan ut eu quam.
        """

    },
    {
        "slug": "Play-with-python",
        "image": "django.png",
        "author": "Nadine",
        "date": date(2021, 6, 16),
        "title": "Programming",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec porta ligula. Quisque sem nisi, scelerisque sit amet pellentesque non,",
        "content": """
            Duis elementum lacus eu sapien ornare, id pharetra mi dignissim.
            Praesent nec eros commodo lacus dignissim eleifend non nec eros.
            Nulla vitae ante id ligula convallis viverra. 
            Curabitur eleifend pretium enim, eget porta sapien mollis et.
            Aliquam sagittis mi neque, ac venenatis enim pretium et.
            Aliquam quis blandit mauris, et ullamcorper nibh. 
            Vivamus laoreet metus eu nisi sollicitudin accumsan ut eu quam.
        """

    },

    {
        "slug": "Play-with-pooh",
        "image": "pooh.png",
        "author": "Nadine",
        "date": date(2021, 6, 16),
        "title": "Winnie The Pooh",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec porta ligula. Quisque sem nisi, scelerisque sit amet pellentesque non,",
        "content": """
            Duis elementum lacus eu sapien ornare, id pharetra mi dignissim.
            Praesent nec eros commodo lacus dignissim eleifend non nec eros.
            Nulla vitae ante id ligula convallis viverra. 
            Curabitur eleifend pretium enim, eget porta sapien mollis et.
            Aliquam sagittis mi neque, ac venenatis enim pretium et.
            Aliquam quis blandit mauris, et ullamcorper nibh. 
            Vivamus laoreet metus eu nisi sollicitudin accumsan ut eu quam.
        """

    },
]


def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
