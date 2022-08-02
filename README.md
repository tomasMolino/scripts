<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->








## Find and Replace Python Script




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Script</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE SCRIPT -->
## About The Script

This script will help you find a word and replace it inside a directory.

There are two main functionalities for this script

* Find and replace a word in the files content of a directory.
* Find and replace a word inside files names of a directory.


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
  ```sh
  pip install python
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* template
 ```commandline
   python script_path find replace mode
```

Let's talk about the parameters:
* find: Is a string, is the one that will be find inside the files of a directory.
* replace: is a string, is the one that will replace the 'find' parameter.
* mode: This parameter tell the script to decide what you want to do.
There are two options
    * place "1" if you want to change the content of the files.
    * place "2" if you want to change the filenames.
   

* EXAMPLE 1:
 ```commandline
   python C:\Users\tm36076\find_replace_script.py plane car 1
```

This will change the word "plane" with the word "car" inside the file.

* EXAMPLE 2:
 ```commandline
   python C:\Users\tm36076\find_replace_script.py "a plane" "a car" 1
```

If you need to change a sentence, like in this case "a plane", you have to place the sentence you
want to replace between "", so that the space can be taken as a character.

<p align="right">(<a href="#top">back to top</a>)</p>







