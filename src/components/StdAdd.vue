<template>
    <div class="container mt-2">
      <h1 style="font-weight: 1000" class="text-center">เพิ่มรายวิชา</h1>
      <form @submit.prevent="addSubject">
        <div class="form-group">
        <label for="termSelect">เลือกภาคเรียน:</label>
        <select class="form-control" v-model="selectedTerm" id="termSelect">
            <option value="std01">ภาคต้น 2565</option>
            <option value="std02">ภาคปลาย 2565</option>
        </select>
        </div>
        <div class="form-group">
          <label for="id">รหัสวิชา:</label>
          <input type="text" class="form-control" id="id" v-model="newSubject.id" required>
        </div>
        <div class="form-group">
          <label for="nameTH">ชื่อวิชา (ภาษาไทย):</label>
          <input type="text" class="form-control" id="nameTH" v-model="newSubject.nameTH" required>
        </div>
        <div class="form-group">
          <label for="nameENG">ชื่อวิชา (ภาษาอังกฤษ):</label>
          <input type="text" class="form-control" id="nameENG" v-model="newSubject.nameENG" required>
        </div>
        <div class="form-group">
          <label for="credit">หน่วยกิต:</label>
          <input type="text" class="form-control" id="credit" v-model="newSubject.credit" required>
        </div>
        <div class="form-group">
          <label for="GPA">เกรดเฉลี่ย (GPA):</label>
          <input type="text" class="form-control" id="GPA" v-model="newSubject.GPA" required>
        </div>

        <br/>
        <button type="submit" class="btn btn-outline-success">บันทึก</button>
      </form>
    </div>
</template>
  
  <script>
  export default {
    name: 'StdAdd',
    data() {
      return {
        newSubject: {
          id: '',
          nameTH: '',
          nameENG: '',
          credit: '',
          GPA: '',
        },
        selectedTerm: 'std01'
      }
    },
    methods: {
  addSubject() {
    if (this.selectedTerm === 'std01') {
      this.addSubjectToTerm('std01');
    } else if (this.selectedTerm === 'std02') {
      this.addSubjectToTerm('std02');
    }
  },
  addSubjectToTerm(term) {
        fetch(`http://localhost:3000/${term}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.newSubject)
        })
        .then(response => {
        if (!response.ok) {
            throw new Error('ไม่สามารถเพิ่มรายวิชาได้');
        }
        // ล้างข้อมูลในฟอร์มหลังจากเพิ่มรายวิชาสำเร็จ
        this.newSubject.id = '';
        this.newSubject.nameTH = '';
        this.newSubject.nameENG = '';
        this.newSubject.credit = '';
        this.newSubject.GPA = '';
        // ส่งสัญญาณไปบอก Component ที่เรียกว่า Add แล้ว
        this.$emit('added');
          alert('บันทึกสำเร็จ');
        })
        .catch(error => {
        console.error('มีข้อผิดพลาดในการเพิ่มรายวิชา:', error);
        });
    }
    }
  }
  </script>
  
  <style scoped>
  .container {
    font-family: Arial, sans-serif;
  }
  </style>