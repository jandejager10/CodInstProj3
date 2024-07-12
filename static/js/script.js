// Initialize Materialize components
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the navbar dropdown
    var elemsDropdown = document.querySelectorAll('.dropdown-trigger');
    var instancesDropdown = M.Dropdown.init(elemsDropdown, {
        coverTrigger: false
    });

    // Initialize the sidenav
    var elemsSidenav = document.querySelectorAll('.sidenav');
    var instancesSidenav = M.Sidenav.init(elemsSidenav);

    // Initialize the datepicker
    var elemsDatepicker = document.querySelectorAll('.datepicker');
    var instancesDatepicker = M.Datepicker.init(elemsDatepicker, {
        format: 'yyyy-mm-dd',
        autoClose: true
    });

    // Initialize the select
    var elemsSelect = document.querySelectorAll('select');
    var instancesSelect = M.FormSelect.init(elemsSelect);

    // Initialize the modal
    var elemsModal = document.querySelectorAll('.modal');
    var instancesModal = M.Modal.init(elemsModal);

    // Initialize tooltips
    var elemsTooltip = document.querySelectorAll('.tooltipped');
    var instancesTooltip = M.Tooltip.init(elemsTooltip);

    // Initialize collapsibles
    var elemsCollapsible = document.querySelectorAll('.collapsible');
    var instancesCollapsible = M.Collapsible.init(elemsCollapsible);
});
