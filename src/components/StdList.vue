<template>
  <h3 style="font-weight: 600"> ภาคต้น 2565 </h3>
   <div class="col" style="padding: 12px 0px"> 
    <h6 v-for="(subj,id) in students" :key="id">
      <div style="padding-bottom: 8px">
        <div style="border:2px solid Tomato;" class="card" @dblclick="toggleDetail(subj)">
          <div class="row" style="padding: 20px">
            <div class="col-8 col-md-2 grade_detail">
              <span style="font-weight: 600"> {{ subj.id }} </span>
            </div>

            <div class="col-4 col-md-2 grade_detail grade_center">
              <span>{{ subj.credit }} </span>
            </div>

            <div class="col-8 col-md-5 border_grade">
              <p class="grade_Text_600" style="margin-bottom: 0px">
                {{ subj.nameTH }}
              </p>
              <span class="grade_subject"> {{ subj.nameENG }} </span>
            </div>

            <div class="col-4 col-md-2 grade_char">
              <span style="font-weight: 520"> {{ subj.GPA }} </span>
            </div>

          </div>
          <span v-if="subj.isshow" >
              <div class="container">
                <p>
                  <button class="btn btn-danger" @click="toggleEdit(subj)">แก้ไขเกรด</button>

                  <button class="btn btn-danger mx-1" @click="delDetail(subj)">ลบรายวิชา</button>
                </p>
                  
                
              </div>
          </span>
          
          </div>
      </div>
      <div class="text-end">
        <span v-if="subj.editing">
          <button class="btn btn-outline-success " @click="subj.newGPA='A'"> A</button> 
          <button class="btn btn-outline-success " @click="subj.newGPA='B+'"> B+ </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='B'"> B </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='C'"> C </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='C+'"> C+ </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='D'"> D </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='D+'"> D+ </button>
          <button class="btn btn-outline-success " @click="subj.newGPA='F'"> F </button>
          <button class="btn btn-success " @click="saveEdit(subj)">บันทึก</button>
        </span>
      </div>

     
      
     
    </h6>

  </div>

  

  
</template>

<script>
export default {
  name: 'StdList',
  components :{

  },
  data() {
    return {
      students:[],
    }
  },
  mounted(){
    fetch('http://localhost:3000/std01')
    .then(res=>res.json())
    .then(data=> {
      data.forEach(subj => {
        subj.editing = false;
        subj.newGPA = subj.GPA;
      });
       this.students=data;
    })
    .catch(err=>console.log(err.message))
    },
    
  methods: {
    toggleDetail(subj) {
      subj.isshow =! subj.isshow;
      subj.editing = false;
    },

    toggleEdit(subj) {
        subj.editing =! subj.editing;
      },
    saveEdit(subj) {
        subj.GPA = subj.newGPA;
        subj.editing = false;
      },
    delDetail(subj) {
        // ส่งคำขอ DELETE ไปยังเซิร์ฟเวอร์เพื่อลบรายการวิชา
        fetch('http://localhost:3000/std01/' + subj.id, {
          method: 'DELETE'
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('ไม่สามารถลบรายการวิชาได้');
          }
          // ลบรายการวิชาที่ถูกลบออกจากข้อมูล
          const index = this.students.findIndex(item => item.id === subj.id);
          if (index !== -1) {
            this.students.splice(index, 1); // แก้ไขนี่
          }
        })
        .catch(error => {
          console.error('มีข้อผิดพลาดในการลบรายการวิชา:', error);
        });
      }
}


  }
  
</script>