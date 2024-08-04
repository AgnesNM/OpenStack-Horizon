(function () {
  'use strict'

angular
  .module('horizon.app.core.images')
  .controller('horizon.app.core.images.DrawerController', controller);

controller.$inject = [
  'horizon.app.core.openstack-service.api.glance',
  'horizon.app.core.images.resourceType'
];

}

  
