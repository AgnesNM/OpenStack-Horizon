// Attempt 1 

ctrl.imageStatusOptions = [
      { label: gettext('Active'), value: 'active' },
    ];

getStatuses();

 function getStatuses() {
      policy.ifAllowed({rules: [['image', 'deactivate_image']]}).then(
        function() {
          ctrl.imageStatusOptions.push({ label: gettext('Deactivate'), value: 'deactivate' });
        }
      );
      policy.ifAllowed({rules: [['image', 'reactivate_image']]}).then(
        function() {
          ctrl.imageStatusOptions.push({ label: gettext('Reactivate'), value: 'reactivate' });
        }
      );
    }
