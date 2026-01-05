document.addEventListener('DOMContentLoaded', function(){
  const grid = document.getElementById('peopleGrid');
  if(!grid) return;

  // Simple demo: toggle showing only Members in 'Current' group when clicking first button
  const btns = document.querySelectorAll('.oval-filter');
  btns.forEach((b, i)=>{
    b.addEventListener('click', ()=>{
      if(i===0){ // group filter: toggle Current members
        const showOnly = b.classList.toggle('active');
        [...grid.children].forEach(card=>{
          const groups = (card.dataset.groups||'').split(',').map(s=>s.trim());
          if(!showOnly) { card.style.display = ''; return }
          if(groups.includes('Current')) card.style.display = ''; else card.style.display = 'none';
        });
      } else { // interest filter: no-op demo (could open dropdown)
        alert('Research-interest filter: implement dropdown or multi-select to filter by interest.');
      }
    });
  });
});
