import names

from subscribers.services.subscriber_service import subscriberService


class SubscriberSeeder(object):

    def seedSubscriber(self,
                       seedProfile=True,
                       seedGhostBlog=True,
                       seedPost=True,
                       seedSneaker=True,
                       seedSneakerRack=True,
                       seedLikedPost=True,
                       getContext=False,
                       ):

        SUBSCRIBER_DICT = {
            'alias': names.get_full_name(),
            'isActive': True,
        }

        # returns seeded context
        context = {}

        subscriber = subscriberService.createNewSubscriber(filters=SUBSCRIBER_DICT)
        context['subscriber'] = subscriber

        # seed profile if it doesn't exist
        if seedProfile:
            from accounts.seed import profileSeeder
            profile = profileSeeder.seedProfile(subscriber=subscriber)
            context['profile'] = profile


        # seed ghost blog that belongs to the subscriber
        if seedGhostBlog:
            from blog.seed import blogSeeder
            blog = blogSeeder.seedBlog(subscriber=subscriber)
            context['blog'] = blog

        # seed post
        if seedPost:
            from posts.seed import postSeeder
            post = postSeeder.seedPost(subscriber=subscriber)
            context['post'] = post

        # seed sneaker
        if seedSneaker:
            from sneaker_rack.seed import sneakerSeeder
            sneaker = sneakerSeeder.seedSneaker(subscriber=subscriber)
            context['sneaker'] = sneaker

        # seed sneaker rack
        if seedSneakerRack:
            from sneaker_rack.seed import rackSeeder
            rack = rackSeeder.seedSneakerRack(subscriber=subscriber)
            context['sneakerRack'] = rack

        # seed Liked Post
        if seedLikedPost:
            from posts.seed import likeSeeder
            like = likeSeeder.seedLike(likedBy=subscriber, post=context['post'] or None)
            context['like'] = like

        return context if getContext else subscriber


subscriberSeeder = SubscriberSeeder()
