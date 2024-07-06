const drag = (event) => {
    event.dataTransfer.setData("text/plain", event.target.id);
  }
  
  const allowDrop = (ev) => {
    ev.preventDefault();
    if (hasClass(ev.target,"dropzone")) {
      addClass(ev.target,"droppable");
    }
  }
  
  const clearDrop = (ev) => {
      removeClass(ev.target,"droppable");
  }
  
  const drop = (event) => {
    event.preventDefault();
    const data = event.dataTransfer.getData("text/plain");
    const element = document.querySelector(`#${data}`);
    const newStatus = event.target.getAttribute('data-status');

    if (!element) {
        console.error("Element not found for ID:", data);
        return;
    }

    try {
        event.target.removeChild(event.target.firstChild);
        event.target.appendChild(element);
        unwrap(event.target);
    } catch (error) {
        console.warn("Can't move the item to the same place:", error);
    }
    
    jQuery.ajax({
        url: '/update_task_status/',
        method: 'POST',
        data: {
            task_id: data.split('-')[1],
            new_status: newStatus,
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        success: (response) => {
            console.log('Status updated successfully:', response);
        },
        error: (xhr, status, error) => {
            console.error('Error updating status:', error);
        }
    });

    updateDropzones();
};


  
  const updateDropzones = () => { 
      var dz = $('<div class="dropzone rounded" ondrop="drop(event)" ondragover="allowDrop(event)" ondragleave="clearDrop(event)"> &nbsp; </div>');
      
      $('.dropzone').remove();
  
      dz.insertAfter('.card.draggable');
      
      $(".items:not(:has(.card.draggable))").append(dz);
  };
  
  function hasClass(target, className) {
      return new RegExp('(\\s|^)' + className + '(\\s|$)').test(target.className);
  }
  
  function addClass(ele,cls) {
    if (!hasClass(ele,cls)) ele.className += " "+cls;
  }
  
  function removeClass(ele,cls) {
    if (hasClass(ele,cls)) {
      var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
      ele.className=ele.className.replace(reg,' ');
    }
  }
  
  function unwrap(node) {
      node.replaceWith(...node.childNodes);
  }
  