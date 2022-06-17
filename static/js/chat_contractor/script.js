window.addEventListener('DOMContentLoaded', function() {


  document.querySelectorAll('.block__tasks').forEach (function(blockTasks) {
    blockTasks.addEventListener('click', function(e) {
      const path = e.currentTarget.dataset.path;

      document.querySelectorAll('.block__tasks').forEach (function(blockTasks) {
        blockTasks.classList.remove('block__tasks-active')
      })
      document.querySelector(`[data-path="${path}"]`).classList.add('block__tasks-active')

      document.querySelectorAll('.content__chat').forEach (function(contentUser) {
        contentUser.classList.remove('content__user-active')
      })
      document.querySelector(`[data-target="${path}"]`).classList.add('content__user-active');
    })
  })
})