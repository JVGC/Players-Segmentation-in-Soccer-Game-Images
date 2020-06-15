# Players-Segmentation-in-Soccer-Game-Images

# **Students**
João Victor Garcia Coelho - 10349540

Paulo André de Oliveira Carneiro - 10295304

# **Abstract**
This project aims to develop and algorithm to separate players from the background and the crowd and subsequently draw the offside line. We'll use Image Segmentation Methods for this.
# **Goal**

Our main goal with this work is to be able to draw the offside lines. To achieve this goal, we opted to work on screenshoots of FIFA game matches, due to the ease of acquiring these images and the image quality itself. To achieve this goal we will use several image processing techniques, such as edge detecting approach along with a hought transformation to separate the field from other elements such as the crowd.

## **Inputs**:

As mentioned above, as input our algorithm expect screenshoots from FIFA game matches. The screenshoot must have the perspective from above.

## **Steps**:

**First Step:** The first step is to extract the field area, so we can then differentiate players and other people from outside the field, such as coaches, reserve players, human-sideline referees, etc. 
   
  - We do that by using Line Detection algorithms such as Hough Transform to identify the top and bottom line of the field. All the pixels below the top line is considered field area. Here we used an Edged Detection Algorithm known as Canny, and then we used a Morphological Operation, known as Dilation on the edges founded, before we used this final image to detect the lines.
  - For sidelines, we don't know yet, because in the images, most sidelines are not vertical, and we have other lines found on the field that can be detect by the algorithm. 
  
  **Next Steps:** The next steps are going to be the extraction of the players in the image, differentiating it from the field, the referee, and the players from each team.
  
  Here we plan to use other image segmentation algorithms, morphological operations, color analysis, and maybe the information of the jersey color.


# **Image Examples**
In this project we're going to use the FIFA game-play images, that provides fair approximation in simulating real-life
soccer scenarios.

![](https://s2.glbimg.com/0qhFV7_YAiJL05DYVP-X0znwRRg=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2018/R/v/ixxop1RH2w2001JJVZIA/44733971-2029113327151462-4091348630277980160-o.jpg)

![](/images/topCrowd5.jpg)


# **First Results**

The First Results Code can be encountered in [Field Line Detection](/Field%20Line%20Detection.ipynb).

## **Original Image**

![Original Image](/images/topCrowd1.jpg)

## **Line Detected Image**

![Line Detected Image](/images/topCrowd1-LineDetected.jpg)

As we can see in the image above, we were able to remove the non-field elements, so on the future, our algorithms will only focus into the elements that are relevant to achiev our main goal, draw the offside line.
