Parts Implemented by Rıdvan SIRMA
=================================
“BLOGS”, “JOBS”, “FEEDS” and “FEEDTYPES” tables are created by me.

Blogs table:

   Columns:

      ID SERIAL PRIMARY KEY,

      USERID INTEGER REFERENCES SITEUSER (USERID),

      DATE DATE NOT NULL DEFAULT CURRENT_DATE,

      HEADER VARCHAR(80) NOT NULL,

      TEXT TEXT NOT NULL

Jobs table:

   Columns:

      ID SERIAL PRIMARY KEY,

      USERID INTEGER REFERENCES SITEUSER (USERID),

      DATE DATE NOT NULL DEFAULT CURRENT_DATE,

      HEADER VARCHAR(80) NOT NULL,

      DESCRIPTION TEXT NOT NULL

Feeds table:

   Columns:

      DATE DATE NOT NULL DEFAULT CURRENT_DATE,

      USERID INTEGER REFERENCES SITEUSER (USERID),

      BOOKID INTEGER REFERENCES BOOKS (ID) ON DELETE CASCADE,

      TYPEID INTEGER REFERENCES FEEDTYPES (ID)

Feed Types table:

   Columns:

      ID SERIAL PRIMARY KEY,

      TYPE TEXT NOT NULL



“BlogPost”, “Job”, “Feed” and “FeedType” classes are owned by me.

I have worked in “BlogPost.py”, “Job.py”, “Feed.py”, “FeedType.py” and “server.py” sources





BlogPost.py:

   Functions:

      -‘insert_blogPost’ function used for insert a new tuple to ‘Blogs’ table. It takes a ‘cursor’ object and ‘BlogPost’ object as a parameter.

      -‘getPost’ function used for get a tuple from ‘Blogs’ table. It takes a ‘cursor’ object and integer value(id) as a parameter. It returns the tuple whose ID is equal to integer parameter.

      -‘getAllPost’ function used for get all tuples from ‘Blogs’ table. It takes a ‘cursor’ object as a parameter. It returns the all tuples.

      -‘deletePost’ function used for delete a tuple from ‘Blogs’ table. It takes a ‘cursor’ object and integer value(id) as a parameter. It deletes the tuple whose ID is equal to integer parameter.

      -‘updatePost’ function used for update a tuple in ‘Blogs’ table. It takes a ‘cursor’ object, one string called ‘text’, one integer called ‘id’ and one date called ‘date’ as a parameter. It updates the tuple whose ID is equal to integer parameter.

      -‘getUserIdFromId’ function used for get the user’s id from ‘Blogs’ table. It takes a ‘cursor’ object and one integer called ‘id’ as a parameter. It returns the id of user who is writer of blog.

Job.py:

   Functions:

      -‘insertJob’ function used for insert a new tuple to ‘Jobs’ table. It takes a ‘cursor’ object and instance of ‘Job’ class as a parameter.

      -‘getJob’ function used for get a tuple from ‘Jobs’ table. It takes a ‘cursor’ object and integer value(id) as a parameter. It returns the tuple whose ID is equal to integer parameter.

      -‘getAllJob’ function used for get all tuples from ‘Jobs’ table. It takes a ‘cursor’ object as a parameter. It returns the all tuples.

      -‘deleteJob’ function used for delete a tuple from ‘Jobs’ table. It takes a ‘cursor’ object and integer value(id) as a parameter. It deletes the tuple whose ID is equal to integer parameter.

      -‘updateJob’ function used for update a tuple in ‘Jobs’ table. It takes a ‘cursor’ object, two strings called ‘description’ and called ‘header’, one integer called ‘id’ and one date called ‘date’ as a parameter. It updates the tuple whose ID is equal to integer parameter.

Feed.py:

   Functions:

      -‘insert_feed’ function used for insert a new tuple to ‘Feeds’ table. It takes a ‘cursor’ object and instance of ‘Feed’ class as a parameter.

      -‘get_all_feeds’ function used for get all tuples from ‘Feeds’ table. It takes a ‘cursor’ object as a parameter. It returns the all tuples.

      -‘get_like_number_of_book function used for get the number of likes of book with id . It takes a ‘cursor’ object as a parameter and an integer value(bookId).

      -‘get_suggestion_number_of_book function used for get the number of suggestions of book with id. It takes a ‘cursor’ object as a parameter and an integer value(bookId).

FeedType.py

   Functions:

      -‘insert_feedtype’ function used for insert a new tuple to ‘FeedTypes’ table. It takes a ‘cursor’ object and instance of ‘FeedType’ class as a parameter.

      -‘get_feedtype_by_id function used for select a type of feed from ‘FeedTypes’ table. It takes a ‘cursor’ object and integer value(id) as a parameter. It returns the type of feed whose ID is equal to integer parameter.

server.py:

   Functions:

      -home_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then all interactions selected from ‘Feeds’ table and printed on the ‘home.html’.

      -about_page() function directs the user to ‘aboutus.html’.

      -jobs_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then it checks whether the user is admin or not. If the user is admin, s/he receive the page that has the whole process like edit and delete. If the user is not admin, then s/he will only display job posting.

      -describe_job_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then it checks whether the user is admin or not. If the user is admin, s/he can write a job posting.

      -describe_job_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then it checks whether the user is admin or not. If the user is admin, s/he can write a job posting.

      -update_job_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then it checks whether the user is admin or not. If the user is admin, s/he can update the job posting which selected in the ‘jobs page’.

      -blogs_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, s/he can see all post , and s/he can delete and update any post.

      -write_post_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then s/he can write post about anything.

      -update_post_page() function firstly checks whether the user log in or not. If user has not logged in, then user redirected to ‘about us page’. If user has logged in, then s/he can update post which selected from the ‘blog page’.
















