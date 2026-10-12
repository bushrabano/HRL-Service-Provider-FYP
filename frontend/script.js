function toggleMenu(){const n=document.getElementById('navMenu');if(n)n.classList.toggle('open');}

document.addEventListener('DOMContentLoaded',()=>{
 const bookingForm=document.getElementById('bookingForm');
 if(bookingForm){
  const date=bookingForm.querySelector('input[type="date"]');
  if(date){date.min=new Date().toISOString().split('T')[0];}
  bookingForm.addEventListener('submit',e=>{
   e.preventDefault();
   const msg=document.getElementById('bookingMessage');
   const name=document.getElementById('bookingName').value.trim();
   const service=document.getElementById('serviceSelect').value;
   const booking={name,service,date:date.value,createdAt:new Date().toISOString()};
   localStorage.setItem('hrl_last_booking',JSON.stringify(booking));
   msg.textContent='Booking request submitted successfully. Our team will contact you.';
   bookingForm.reset();
  });
 }
 const contactForm=document.getElementById('contactForm');
 if(contactForm){
  contactForm.addEventListener('submit',e=>{
   e.preventDefault();
   document.getElementById('contactMessage').textContent='Your message has been sent successfully.';
   contactForm.reset();
  });
 }
 const loginForm=document.getElementById('loginForm');
 if(loginForm){
  loginForm.addEventListener('submit',e=>{
   e.preventDefault();
   document.getElementById('loginMessage').textContent='Demo login successful. Connect a backend for real authentication.';
  });
 }
});

function showSignup(e){
 e.preventDefault();
 alert('Signup page can be added when the backend authentication module is connected.');
}

document.addEventListener('DOMContentLoaded',()=>{
 const select=document.getElementById('serviceSelect');
 if(select){
  const slug=new URLSearchParams(location.search).get('service');
  const map={'plumbing':'Plumbing','electrician':'Electrician','cleaning':'Cleaning','painter':'Painter','car-repair':'Car Repair','care-services':'Care Services','tutor':'Tutor','it-support':'IT Support'};
  if(slug && map[slug]) select.value=map[slug];
 }
});
