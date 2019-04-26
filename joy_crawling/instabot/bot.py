import instapy
session = instapy.InstaPy(username="", password="")
session.login()
#session.like_by_tags(['love'],amount=1000,media='Photo')
try:
    #팔로우봇
    session.follow_by_tags(['선팔','맞팔','팔로우'], amount=50)
    #좋아요봇
    session.like_by_feed(amount=1000, randomize=True, unfollow=False, interact=True)
except:
    raise





#https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md#liking
#https://github.com/timgrossmann/InstaPy
