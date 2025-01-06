<template>
  <ul class="nav nav-tabs" id="myTab" role="tablist">
  <li class="nav-item" role="presentation">
      <p class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane"
        role="tab" aria-controls="home-tab-pane" aria-selected="true">Home</p> 
  </li>
  </ul>

<div class="container mt-5"> 
    <h1 class="text-center" style="color: brown; font-size : 70px">PORTFOLIO</h1>
      <div style="background-color: peachpuff;">
        <div class="text-center">
          <div class="col" style="padding: 12px 0px"> 
            <div style="padding-bottom: 8px">
                <div class="row" style="padding: 20px">
                    <div class="col-12 col-md-10" style="display: flex; justify-content: center; align-items: center;">
                        <img alt="" src="./assets/punch.jpg" width="300" style="margin-right: 100px;">
                        <div style="display: inline-block;">
                            <h3 class="grade_Text_600" style="margin-right: 20px; font-size :40px" >{{ major }}</h3>
                              <span style="font-size :20px">{{ university }}</span><br>
                              <h3 style="margin-top: 30px">
                                <button class="btn btn-outline-dark mx-1" @click="ShowHistory()">About Me</button> <br>
                             
                              </h3>
                              
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>          
</div>

<div v-if="hisdata" >
  <div class="container mt-5">
    <div style="border-style: double; border-radius: 10px; border: 2px solid ">
        <div class="text-center">
          <div class="col" style="padding: 12px 0px"> 
            <div style="padding-bottom: 8px">
                <div class="row" style="padding: 20px">
                    <div class="col-12 col-md-10" style="display: flex; justify-content: center; align-items: center;">
                      <img alt="" src="./assets/babypunch.jpg" width="150" style="margin-right: 100px;">
                                    <p class="text-start">   
                                        name : {{ name }} <br>
                                        nickname : {{ nickname }} <br>
                                        birthday : {{ date }} <br>
                                        hobbies : {{ hobbies }} 

                                    </p> 
                                          
                    </div>
                  </div>
              </div>
          </div>
        </div>
      </div>
  </div>
</div>
      
    <br>
    <button class="btn btn-success mx-1" @click="ShowData()">แสดงผลการเรียน</button >
    <button class="btn btn-success mx-1" @click="ShowAdd()">เพิ่มรายวิชา</button >
    <div v-if="showStdList" class="m-2">
      <StdList/>
      <StdList2/>
    </div>

    <div v-if="showAddStd" class="m-2">
      <StdAdd/>
    </div>

  </div>

  
  
 
  
</template>

<script>

import StdList from './components/StdList.vue' 
import StdList2 from './components/StdList2.vue' 
import StdAdd from './components/StdAdd.vue' 

export default {
  name: 'App',
  components: {
    StdList,
    StdList2,
    StdAdd
  },
  data() {
    return {
      name :'Manitchaya Benjajerdisi',
      nickname:'punchii',
      hobbies:'ดู series แบบฉ่าม และ นอนจำศีล ',
      date : '6 พฤษาคม 2547',
      id :'65302000380',
      major:'Computer Science',
      university :'kasetsart university sriracha campus ',
      showStdList: false,
      showAddStd : false,
      hisdata : false
      
    }
  },
  methods : {
    ShowData() {
      this.showStdList =! this.showStdList
      this.showAddStd = false
    },
    ShowAdd () {
      this.showAddStd =! this.showAddStd
      this.showStdList = false
    },
    ShowHistory() {
      this.hisdata =! this.hisdata
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #502c47;
  
}
</style>
