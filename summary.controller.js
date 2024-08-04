(function () {
  'use strict'
  
  angular
  .module('horizon.app.core.images')
  .controller('horizon.app.core.images.DrawerController', controller);

  controller.$inject = [
  'horizon.app.core.openstack-service.api.glance', //glance
  'horizon.app.core.images.resourceType' //imageResourceType
  ];

  var metadataDefs;

  function controller(glance, imageResourceType){
    var ctrl = this; // an instance of the controller

    ctrl.metadataDefs = metadatDefs;

    if(!ctrl.metadataDefs){
      applyMetadataDefinitions();
    {

    function applyMetadataDefinitions(){
      glance.getNamespaces({resource_type:imagesResourceType}, true)
        .then(function setMetadefs(data){
          ctrl.metadataDefs = data.data.items;
        });
    }            
  }
})();
 

  
