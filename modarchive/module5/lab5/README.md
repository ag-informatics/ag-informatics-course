# Module 5, Lab 5

## Before the Lab
Make sure you are familiar with the following concepts before you begin this section:

1. How to use the [`extends`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatetag-extends) tag in Django. 
   - If you are not familiar with these, revisit the [CS50 video from last module](https://github.com/ag-informatics/ag-informatics-course/tree/main/module4), as it contains an example of how to use the `extends` tag at least.
   - Note, there is also an [`include`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatetag-include) tag that does similar things, but in a slightly different manner.
   - [Here's a helpful discussion](https://stackoverflow.com/questions/2863695/include-vs-extends-in-django-templates) on the difference between the two.

2. We briefly discussed the Bootstrap framework in class. Make sure you are comfortable with the concept of different components in Bootstrap.
   - In particular, review the [Bootstrap container](https://getbootstrap.com/docs/4.3/layout/overview/), the different [components](https://getbootstrap.com/docs/4.3/components/alerts/), and at least know what the [basic changes being made to your basic elements](https://getbootstrap.com/docs/4.3/content/reboot/). 

3. I gave a quick demo of how to integrate Boostrap into a Django app, and my code is [available here, in this module's folder](https://github.com/ag-informatics/ag-informatics-course/tree/main/module5/bootstrap-demo). The video is on Brightspace if you'd like to review.
   - Here's a good tutorial on Django + Bootstrap if you are stuck: https://www.ordinarycoders.com/django-bootstrap

### Lab Submission Folder Structure
You will be submitting a few different things. Create a folder called **'lab5'**. Create a subfolder called **'paper-protoype'** and copy over your previous lab 5.

```
lab5/
  paper-prototype/
  ACRE/         # Copy over your previous project, you'll be building on it.
  README.md
```

## Part 1: Paper Prototpying
During Lecture 5.3 (Tuesday, Oct 26), you will bring a paper prototype of a new feature you'd like to test out for the ACRE Farm Management App you built in Module 4. I will provide feedback and you will do some "lite" user testing on your prototype. As you are watching people "use" your prototype, make notes so that you can answer a questions listed below in your README.MD file

> In your README.MD file, create a heading called "Paper Prototype User Feedback", and describe, in brief:
> - Where did users get stuck?
> - Where did users seem to gain the most value (joy, usefulness, or something else)?
> - What are three things you would improve on your app?

Revise your prototype based on the feedback you receive.

Next, create a a short (<3 minute) video of your paper prototype. Remember the example show in class, [here's the link again](https://www.youtube.com/watch?v=GrV2SZuRPv0). **Upload the video to brightspace with your final submission.**

## Part 2: Boostrapify your Django app
As shown in class, link the boostrap framework to your Django app, using the BootstrapCDN. [Instructions here.]https://getbootstrap.com/docs/4.3/getting-started/introduction/

In the previous module, you had implemented the ACRE Farm Management app. Now, upgrade each of your views as follows.

### Parent Template
The power of Django templates can allow you to create reusable templates that you can recombine to create pages in different ways.

In this section, we will create a "skeleton" template file, that is, a parent template file, that contains a a header and footer to be reused across all your views. You will then update each of your views to `extend` this template.

Create a file called "skeleton.html", and make sure you include the follwoing:

1. The title of your app, in a striking font. Include a "logo" for the app, by using a relevan icon from the [Noun Project](https://thenounproject.com/).

2. A Boostrap [Navigation Bar](https://getbootstrap.com/docs/4.3/components/navbar/) that contains static links to each of your views. 

3. A [**Container**](https://getbootstrap.com/docs/4.3/layout/overview/) based layout that should work well for all your views. Your dynamic content will be inserted in this "body" area of your skeleton.

4. A footer that contains YOUR NAME and the date the page was last updated.

### Bootstrap Components
Currently, you have at least 3 views represented via **'index.html'** and **'fields.html'**, and your to-be-created **'secretsauce.html'** template. You must use the following Bootstrap components anywhere on your app:

1. [Cards](https://getbootstrap.com/docs/4.3/components/card/)

2. Any of the [Collapse](https://getbootstrap.com/docs/4.3/components/collapse/) classes. For example, you can combine this with Cards to create an [Accordion](https://getbootstrap.com/docs/4.3/components/collapse/#accordion-example)

3. At least 2 [buttons](https://getbootstrap.com/docs/4.3/components/buttons/) for major actions, e.g. "Add a Log Entry", or a button group (https://getbootstrap.com/docs/4.3/components/button-group/).


### Secret Sauce
During your paper-prototyping, you may have come up with some radical ideas to improve your app. I'm going to ask you to implement a SINGLE VIEW to capture some of what your proposed idea was. **Do not make major changes to your model.**

Unless you are ABSOLUTELY confident you can implement this 1-view idea within the lab timeframe, I suggest you discuss your proposed implementation idea with Ankita or Aanis to ensure you're not committing to too much :)

Your view and the resulting template should have the title **'secret-sauce'**. 

> In your README.MD file, create a heading called "Secret Sauce" and describe your first prototpye of a very slimmed down version of your paper-prototyped idea.

## How to Submit your Lab
Your final lab submission should contain the following files:

```
lab5/
  README.md                   <-- you should have all the pieces described in lab here
  paper-prototpye/            <-- however many images you want to upload of your paper prototype
    image1.png
    imageX.png
    video.format              <-- if it's not too big, upload your video here too in whatever format. Otherwise, just upload to Brightspace
  acre/                       <-- your Django project
    manage.py
    acre/                     
    acrelog/                  <-- your lab old Django APP + new lab 5 additions
        fixtures/             
        migrations/
        templates/            
          index.html
          fields.html
          skeleton.html       <-- your skeleton template.
          secret-sauce.html   <-- your new template!
        __init__.py
        admin.py
        apps.py
        models.py             
        tests.py
        urls.py               
        views.py              <-- your new view!
    db.sqlite3
```

GO TO BRIGHTSPACE, submit the link to your repository, and upload your paper prototype video. It is done!

And so concludes our time with Django. It was long and short and hopefully interesting. Nice work!


## Future Learning Pathways 
Mozilla has a really excellent set of tutorials on Django if you'd like to dig deeper and get a more comprehensive look at how to build web apps in Django: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

For a quick end-to-end tutorial/refresh on Django, try: https://www.ordinarycoders.com/build-a-django-web-app 

If we had time, I would have love to cover JavaScript. If you'd like to get acquainted, here's a good set of starter materials:
 - Mozilla: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
 - CS50 actually builds on Django with Javascript, so you can try it too: https://cs50.harvard.edu/web/2020/weeks/5/

## License
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<!-- This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] -->

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

  "Introduction to Agricultural Informatics Course" by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.](http://creativecommons.org/licenses/by-nc-sa/4.0/)