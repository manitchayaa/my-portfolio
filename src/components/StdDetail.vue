<template>
  <div class="container ">
    <p >
      <button class="btn btn-danger" @click="editDetail()">แก้ไขข้อมูล</button>
    </p>
    
  </div>
    
</template>

<script>
export default {
  name: 'StdDetail',
  data(){
    return {
      students:[]
    }
  },
  methods:{
    editDetail() {
      this.$emit('edit')
    }
  }
}

</script>