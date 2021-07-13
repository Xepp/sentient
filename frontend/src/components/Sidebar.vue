<template>
  <div class="panel-sidebar shadow px-3">
    <router-link
      v-for="item in items"
      :key="item.routeName"
      class="nav-item d-flex justify-content-end align-items-center p-1"
      :to="{ name: item.routeName }"
    >
      <div> {{ item.title }} </div>
      <img
        :src="item.imageLogo"
        :alt="item.imageAlt"
        class="rounded-lg ml-2"
        width="60"
      />
    </router-link>
  </div>
</template>

<script>
import KhabarFooriLogo from '@/assets/khabar-foori-logo.png'
import TelegramLogo from '@/assets/telegram-logo.svg'
import InstagramLogo from '@/assets/instagram-logo.svg'
import TwitterLogo from '@/assets/twitter-logo.svg'

export default {
  name: 'Sidebar',
  computed: {
    items: () => ([
      {
        routeName: 'KhabarFoori',
        imageLogo: KhabarFooriLogo,
        imageAlt: 'Khabar Foori',
        title: 'خبر فوری'
      },
      {
        routeName: 'Instagram',
        imageLogo: InstagramLogo,
        imageAlt: 'Instagram',
        title: 'اینستاگرام'
      },
      {
        routeName: 'Twitter',
        imageLogo: TwitterLogo,
        imageAlt: 'Twitter',
        title: 'توییتر'
      },
      {
        routeName: 'Telegram',
        imageLogo: TelegramLogo,
        imageAlt: 'Telegram',
        title: 'تلگرام'
      }
    ])
  }
}
</script>
