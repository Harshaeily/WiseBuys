document.getElementById('signUpBtn').addEventListener('click', function() {
  document.querySelector('.signup-box').style.display = 'block';
  document.querySelector('.signin-box').style.display = 'none';
});

document.getElementById('signInBtn').addEventListener('click', function() {
  document.querySelector('.signup-box').style.display = 'none';
  document.querySelector('.signin-box').style.display = 'block';
});
