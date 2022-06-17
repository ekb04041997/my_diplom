window.addEventListener('DOMContentLoaded', function() {

  document.querySelectorAll('.customer__button1').forEach(function(customerButton1) {
    customerButton1.addEventListener('click', function(e) {
      document.querySelectorAll('.block__customer').forEach(function(blockCustomer) {
        blockCustomer.classList.remove('block__noactive')
      })
      document.querySelectorAll('.block__student').forEach(function(blockStudent) {
        blockStudent.classList.add('block__noactive')
      })
    })
  })

  document.querySelectorAll('.student__button2').forEach(function(studentButton2) {
    studentButton2.addEventListener('click', function(e) {
      document.querySelectorAll('.block__student').forEach(function(blockStudent) {
        blockStudent.classList.remove('block__noactive')
      })
      document.querySelectorAll('.block__customer').forEach(function(blockCustomer) {
        blockCustomer.classList.add('block__noactive')
      })
    })
  })
})