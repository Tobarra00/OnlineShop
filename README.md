<header>
    <h1>Online shop 🛒</h1>
</header>

<div>
    <p>This is the <strong>my first <code>Django</code> project</strong> simulating how a simple Online Shop could work. In this project, I have worked with different tools and settings. It is composed of 5 different sections: "HOME", "SERVICES", "SHOP", "CONTACT" and "BLOG". Each one of them has a different level of difficulty in its implementation and I will explain them in ascendent difficulty order. However, the first step is to clone the repository and make it work.
    </p>
</div>

<section>

<h2>How to make it work 🔧</h2>

<p>In this section I will show step by step how to make this code work:</p>
<ol>
    <li>Use <code>git clone</code> to clone the repository or download the <code>OnlineShop</code> directory. After that, open an editor and navigate to the project directory where the <code>OnlineShop</code> directory is. Then create a virtual environment with:<br>
    <code>pip install virtualenv</code><br>
    <code>virtualenv venv</code><br>
    After that, activate the virtual environment and use this command to install the requirements to make the project work properly:<br>
    <code>pip install -r requirements.txt</code><br>
    It should look something like this:
    <br><br>
    <img src="images/Project directory.png" alt="Project directory" width="350">
    <br><br>
    </li>
    <li>The next step is to manage the database. I have uploaded the hole database with all the info I have been working on, so there sould not be any problem. In case you want to delete it to create your own stuff, just do it, as the <code>data.json</code> file contains all the info of the original database. I created the file using:<br>
    <code>python manage.py datadump > data.json</code><br>
    <br>
    Which you can later load into your database with:<br>
    <code>python manage.py loaddata data.json</code><br>
    <br>
    Even if you use the default database, you probably should execute these commands before running the server:<br>
    <code>python manage.py makemigrations</code><br>
    <br>
    <code>python manage.py migrate</code><br>
    <br>
    </li>
    <li>To wrap things up, go to the <code>Onlineshop/OnlineShop</code> directory and open the <code>.env.txt</code> file. Here you have to replace the asigned values of the variables with your own data. For example:<br>
        <ul>
            <li>
                In <code>SECRET_KEY=your_secret_key</code>, replace <code>your_secret_key</code> with your secret key, which you can generate by your own or use:<br>
                <code>from django.core.management.utils import get_random_secret_key</code>.
            </li>
            <li>
                In <code>DEBUG=true_or_false</code>, replace <code>true_or_false</code> with the <code>True</code> or <code>False</code>, depending on what you want to do.
            </li>
            <li>
                In <code>TEMPLATES_DIR=templates_directory</code>, replace <code>templates_directory</code> with the path to the directory where you store your django templates.
            </li>
        </ul>
    ⚠️ To make these variables work, just delete the <code>.txt</code> extension of the file.<br><br>
    </li>  
    <li>Finally, if everything went right, you should be able to run the server and visualize the website with all the images and functionalities by using the command:<br>
    <code>python manage.py runserver</code><br><br>
    </li>
    <li>And that's all, you should be able to navigate and try the website with all of its functionallity 😉.<br><br></li>
</ol>
</section>

<section>
    <h2>
        Contact me:
    </h2>
    <p>In case you have any doubt or you are interested about my work, you can contact me here: </p>
    <ul>
        <li>My linkedin: <a href="https://www.linkedin.com/in/pedro-tobarra-leal/"><img src="images/linkedin.png" alt="linkedin" width="20"></a></li>
        <li>My email: <a href="mailto:pedro.tobarra.leal@gmail.com">Pedro.tobarra.leal@gmail.com</a></li>
    </ul>
</section>
