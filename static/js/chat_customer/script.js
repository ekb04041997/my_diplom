window.addEventListener('DOMContentLoaded', function() {


  document.querySelectorAll('.block__tasks').forEach (function(blockTasks) {
    blockTasks.addEventListener('click', function(e) {
      const path = e.currentTarget.dataset.path;

      document.querySelectorAll('.block__tasks').forEach (function(blockTasks) {
        blockTasks.classList.remove('block__tasks-active')
      })
      document.querySelector(`[data-path="${path}"]`).classList.add('block__tasks-active')

      document.querySelectorAll('.content__user').forEach (function(contentUser) {
        contentUser.classList.remove('content__user-active')
      })
      document.querySelector(`[data-target="${path}"]`).classList.add('content__user-active');
    })
  })

  document.querySelectorAll('.block__users').forEach (function(blockUsers) {
    blockUsers.addEventListener('click', function(e) {
      const path = e.currentTarget.dataset.path;

      document.querySelectorAll('.block__users').forEach (function(blockUsers) {
        blockUsers.classList.remove('block__users-active')
      })
      document.querySelector(`[data-path="${path}"]`).classList.add('block__users-active')

      document.querySelectorAll('.content__chat').forEach (function(contentChat) {
        contentChat.classList.remove('content__user-active')
      })
      document.querySelector(`[data-target="${path}"]`).classList.add('content__user-active');
    })
  })



})

function lastMessageScroll(b) {
  var e = document.querySelector('.wrapper__scrollbottom');
  if (!e) return ;

  e.scrollIntoView({
      behavior: b || 'auto',
      block: 'end',
  });
}
