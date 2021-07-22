<template>
  <div class="result-section">
    <template
      v-if="source === 'telegram'"
    >
      <telegram-channel-post
        v-for="post in items"
        :key="post.id"
        class="shadow my-4 mx-auto"
        style="width: 520px; min-height: 260px;"
        :id="post.id"
        :date="post.date"
        :link="post.link"
        :sentiment="post.sentiment"
        :text="post.text"
        :views="post.views"
        username="currentUser"
      ></telegram-channel-post>
    </template>
    <template
      v-else-if="source === 'twitter'"
    >
      <twitter-feed-item
        v-for="item in items"
        :key="item.id"
        class="shadow my-4 mx-auto"
        style="width: 520px; min-height: 260px;"
        :user="item.user"
        :created-at="item.created_at"
        :id="item.id"
        :favorite-count="item.favorite_count"
        :retweet-count="item.retweet_count"
        :sentiment="item.sentiment"
        :text="item.text"
        :tweet-type="item.type"
      ></twitter-feed-item>
    </template>
    <template
      v-else-if="source === 'khabar-foori'"
    >
      <khabar-foori-feed-comment
        v-for="(comment, index) in items"
        :key="index"
        class="shadow my-4 mx-auto"
        style="width: 520px; min-height: 260px;"
        :author="comment.author"
        :date="comment.date"
        :like-count="comment.pos"
        :dislike-count="comment.neg"
        :sentiment="comment.sentiment"
        :text="comment.text"
      ></khabar-foori-feed-comment>
    </template>
    <template
      v-else-if="source === 'instagram'"
    >
      <instagram-post-comment
        v-for="comment in items"
        :key="comment.id"
        class="shadow my-4 mx-auto"
        style="width: 520px; min-height: 200px;"
        :id="comment.id"
        :sentiment="comment.sentiment"
        :text="comment.text"
        :username="comment.username"
        :created-at="comment.created_at"
      ></instagram-post-comment>
    </template>
    <b-button
      v-if="hasMore"
      class="mx-auto"
      style="width: 200px;"
      variant="outline-primary"
      @click="$emit('load-more')"
    > نتایج بیشتر </b-button>
  </div>
</template>

<script>
import TelegramChannelPost from '@/components/TelegramChannelPost'
import TwitterFeedItem from '@/components/TwitterFeedItem'
import KhabarFooriFeedComment from '@/components/KhabarFooriFeedComment'
import InstagramPostComment from '@/components/InstagramPostComment'

export default {
  name: 'ResultSection',
  components: {
    TelegramChannelPost,
    TwitterFeedItem,
    KhabarFooriFeedComment,
    InstagramPostComment
  },
  props: {
    source: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      required: false,
      default: () => []
    },
    hasMore: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>
