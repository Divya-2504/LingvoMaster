

$(document).ready(function () {
    $('.fa-bars').click(function () {
      $(this).toggleClass('fa-times');
      $('.navbar').toggleClass('nav-toggle');
    });
    $(window).on('scroll  load', function () {
      $('.fa-bars').removeClass('fa-times');
      $('.navbar').removeClass('nav-toggle');
      if ($(window).scrollTop() > 30) {
        $('header').addClass('header-active');
      }
      else {
        $('header').removeClass('header-active');
      }
      $('section').each(function () {
        var top = $(window).scrollTop();
        var id = $(this).attr('id');
        var height = $(this).height();
        var top = $(this).offset().top - 200;
        if (top >= offset && top < height + offset) {
          $('.navbar ul li a').removeClass('active');
          $('.navbar').find('[href="#' + id + '"]').addClass('active');
        }
      });
    });
  });
  
  function check(){
    let name=document.form1.nm.value;
    patName=/^[A-z]+$/;
    let  e_mail=document.form1.em.value
    patEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let phone=document.form1.ph.value;
    patPhone= /^\d$/;
    let msg=document.form1.msg.value;
    if(!patName.test(name))
    {
      alert("Username Incorrect")
    }
    else if(!patEmail.test(e_mail)&&e_mail.length==0){
      alert( "Please enter a valid email address");
    }
    else if(!patPhone.test(phone)&& (phone.length==0||phone.length<10||phone.length>10))
    {
      alert("enter a valid phone number")
    }
    else if(msg.length==0){
      alert("Message cannot be empty")
    }else{
        alert("Message Submitted Successfully");
      document.form1.reset();
    }
  }
  
  document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var firstName = document.getElementById('name1').value.trim();
    var lastName = document.getElementById('name2').value.trim();
    var userName = document.getElementById('name3').value.trim();
    var email = document.getElementById('email').value.trim();
    var password = document.getElementById('password').value.trim();
  
    // Regex patterns
    var nameRegex = /^[a-zA-Z]+$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
    // Validate inputs
    if (!nameRegex.test(firstName) || !nameRegex.test(lastName)) {
        alert('Please enter a valid first and last name.');
        return;
    }
  
    if (!userName) {
        alert('Please enter a user name.');
        return;
    }
  
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }
  
    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return;
    }
  
    // Form is valid, proceed with submission
    alert('Form submitted successfully!');
    // You can submit the form here if needed
  });
  function toggleUpdateForm() {
    var updateForm = document.getElementById('updateForm');
    updateForm.style.display = updateForm.style.display === 'none' ? 'block' : 'none';
    if (updateForm.style.display === 'block') {
        // Set input values to current user details
        document.getElementById('newFirstName').value = document.getElementById('firstName').textContent;
        document.getElementById('newLastName').value = document.getElementById('lastName').textContent;
        document.getElementById('newUsername').value = document.getElementById('username').textContent;
        document.getElementById('newEmail').value = document.getElementById('email').textContent;
    }
  }
  
  function updateDetails(event) {
    event.preventDefault();
    var newFirstName = document.getElementById('newFirstName').value;
    var newLastName = document.getElementById('newLastName').value;
    var newUsername = document.getElementById('newUsername').value;
    var newEmail = document.getElementById('newEmail').value;
  
    // Update the user's details (you can perform your update logic here)
    document.getElementById('firstName').textContent = newFirstName;
    document.getElementById('lastName').textContent = newLastName;
    document.getElementById('username').textContent = newUsername;
    document.getElementById('email').textContent = newEmail;
  
    // Close the update form
    toggleUpdateForm();
  }
  
  function logout() {
    // Perform logout actions here
    alert("Logout successful!");
    // Redirect to logout page or perform any other action as needed
  }
  