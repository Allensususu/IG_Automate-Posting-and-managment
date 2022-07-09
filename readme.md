# IG_Automate-Posting-and-managment
An easy way to automate posts and manage your IG accounts

## How to use?

First enter your account password into ``` account.xls ```.

Put the post you want into img, and put the text of the post into the img folder with the same file name txt.Like 123.jpg and 123.txt,the program will automatically pair when sending a message.

open  ``` main.py  ``` and modify what you want to do.
## example 
```login_ig.login(account,password,browser)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function can help you log into instagram automatically.

```otherfunction.read_cookie(browser,account)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function can help you record your cookies, and you can read the cookies when you log in next time, avoiding multiple logins


&nbsp;&nbsp;&nbsp;&nbsp;Use with``` otherfunction.save_cookie(browser,account)```

```otherfunction.get_follower_post(browser,account_name,i)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function can get the number of posts, followers, and number of followers on its own account

```#follow.auto_follow(other_account , browser, post_)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function can automatically track followers of ``` other_account```

```otherfunction.get_follower_post(browser,account_name,i)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function can automatically track ``` account_name```'s tracker

```post.post(browser,account)```

&nbsp;&nbsp;&nbsp;&nbsp;-Function will automatically select the in pairs posts in the img folder. Like 123.jpg and 123.txt,the program will automatically pair when sending a message.