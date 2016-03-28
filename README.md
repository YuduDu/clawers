# clawers
clawers working with ifttt to get pics or videos you like from social media. continue developing

For twitter and Sina Weibo, ifttt don't have working channel can download pics or videos we liked, only thing working even fine is save link to the post . But I really need the function personally, I write some simple code using urllib and beautiful soup to download those medias.

After add necessary parameters in the code, you can use these code create alfred workflows, then those code can be called by a simple command in alfred in the future

# Twitter
you can just add a channel in ifttt to save your liked post's link to a html file. add the path to the folder hold those files in code.

# Sina Weibo
those channel to save your liked post's link is not working well, so do save new post's link to html file and repost posts that you want to save.
And to save pics from weibo is pretty headache, cause it's need authentication... Using cookies is not working for web page, but fortunately it's working for mobile page, so besides save path to ifttt weibo folder, also open your broswer, visit mobile weibo page, login and save cookies in a txt file which you can easily do that with some extension.


