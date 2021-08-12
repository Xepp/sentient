<template>
  <b-container>
    <b-card
      class="mx-auto mt-5 bg-light"
      style="max-width: 30rem;">
      <img
        class="bg-info w-100 mb-3"
        src="@/assets/sadra-logo.png"
      />
      <b-alert
        show
        variant="secondary"
      >
        <p>به سامانه ی شناختی تحلیل فضای مجازی خوش آمدید</p>
        <hr>
        <p class="mb-0">لظفا وارد سیستم شوید</p>
      </b-alert>
      <b-form>
        <b-form-input
          v-model="username"
          class="mt-2"
          id="username"
          type="text"
          placeholder="نام کاربری"
          @input="(v) => invalidCredentials = false"
          @keydown.enter.prevent="login"
        ></b-form-input>
        <b-form-input
          v-model="password"
          class="mt-4"
          id="password"
          type="password"
          placeholder="رمز عبور"
          @input="(v) => invalidCredentials = false"
          @keydown.enter.prevent="login"
        ></b-form-input>
        <b-button
          class="mt-4 w-100"
          :disabled="!username && !password"
          variant="primary"
          @click="login"
        >ورود</b-button>
      </b-form>
      <b-alert
        :show="invalidCredentials"
        class="mt-3"
        variant="danger"
      >اطلاعات وارد شده اشتباه است. لطفا مجددا امتحان کنید</b-alert>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      username: '',
      password: '',
      invalidCredentials: false
    }
  },
  methods: {
    login () {
      if (this.username === 'admin' && this.password === 'admin') {
        this.$router.push({ name: 'Home' })
      } else {
        this.invalidCredentials = true
      }
    }
  }
}
</script>
