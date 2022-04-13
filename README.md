# Blogger

`A django based blogging website`

A blog is a type of website where the content is presented in reverse chronological order (newer content appear first). Blog content is often referred to as entries or “blog posts”. Blogs are typically run by an individual or a small group of people to present information in a conversational style.

## Preview

<a href="https://heroku.blogger.com/">Go to page</a>

**For any reason if the url not working watch the preview below**


### Home page

![home page](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/home%201.png)

Above is the home page which shows lasted posts, recent tags and most viewed posts. We can actually see the details associated with each post over home page.

### Post blog

![post bLog](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/blog%20post%201.png)
![post blog](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/blog%20post%202.png)

Here you can post a blog.

Fields required to submit form:
+ title 
+ content
+ describe
+ tags
+ slug
+ thumbnail


### Post view

![post](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/my%20blog%201.png)
![post](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/my%20blog%202.png)
![post](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/my%20blog%203.png)
![post](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/my%20blog%204.png)

+ Here we can see the post details including content, tags, date paoted, likes, comments and views.
+ Comments to the post can also be viewed in the last of the post.
+ `Users can also comment on the post.`
+ `If the current user is the author of the post then author can also update and delete the post`

### All post of the user can be viewed in side Blog Entries

![blog entries](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/blog%20entries%201.png)

like for the above example anushka have 3 posts and two of them are BSE and Burj Khalifa.

### Search post

![search](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/search.png)

Users can also search post.

### Tags
![search](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/tags.png)
+ Recent tags can be viewed in tag clouds.
+ Tags can also be listed and can be used to search post via tags.

### Search Post by tag
![search](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/tag%20applied.png)
Post searched via tag, in the above example tag used is SPACE


## Most importantly Authntication System

### SignIn / Login page
![login](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/login%20page.png)

Form Requires Username and Password to authenticate. In case if user forget password, it can be easily reset via email.

##### Forget password
![forgetpassword](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/forget%20password.png)

### SignUp / Register page
![register](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/register%20page.png)

### Logout view
![logout](https://github.com/HarshNarwariya/blogger_django_based_web/blob/main/Images/logout%20page.png)
This page ensures that user have been logged out successfully.


### Requirements
```python
pip install Django
pip install django-crispy-forms
pip install django-ckeditor
pip install django-taggit
```
