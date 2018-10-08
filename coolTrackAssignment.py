listOfTweets = []#Holds Object in to list
count = 0#Count for num of User You want to add
class Tweet:
    '''Tweet is Class For User Tweets with Arguments as testcase,tweets,username,tweet_id'''
    def __init__(self,testcase,tweets,username,tweet_id):#
        self.testCase = testcase#Instance Obj==Self.testcae
        self.userTweets = tweets
        self.userName = username
        self.tweetId = tweet_id

    def __str__(self):
        '''This is string Resprentation to print Object'''
        return '{}{}{}'.format(self.userTweets,self.userName,self.tweetId)

    def __repr__(self):
        '''Representation for print Nested Data Structure object'''
        return str

    def nameOfUser(name):
        for item in listOfTweets:
         if (item.count(name)):
          print('Name And Count ',name,count)

testCase = int(input('number of test cases'))
def userTweet():
 while True:
     global count
     if count <testCase:
         tweets = input('number of tweets')
         userName = input('User name')
         tweetId = input('Tweet Id')
         count = count + 1
         listOfTweets.append([tweets ,userName, tweetId])
         print(listOfTweets)

     else:
         break


userTweet()
Tweet.nameOfUser(name=input('Enter the Name of User to get list of Tweets'))

#print(Tweet.__doc__)
'''
Input & Output---

number of test cases2
number of tweets1
User nameAmit
Tweet Id1
[['1', 'Amit', '1']]
number of tweets2
User nameAshish
Tweet Id1
[['1', 'Amit', '1'], ['2', 'Ashish', '1']]
Enter the Name of User to get list of TweetsAshish
Name And Count  Ashish 2
'''