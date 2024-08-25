/**
 * (c) Copyright 2016 Hewlett-Packard Development Company, L.P.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

(function () {
  'use strict';

  angular
    .module('horizon.app.core.images')
    .controller('horizon.app.core.images.steps.DeactivateImageController', DeactivateImageController);

  DeactivateImageController.$inject = [
    '$scope',
    'horizon.app.core.images.imageFormats',
    'horizon.app.core.images.validationRules',
    'horizon.app.core.openstack-service-api.settings',
    'horizon.app.core.openstack-service-api.policy'
  ];

  /**
   * @ngdoc controller
   * @name horizon.app.core.images.steps.DeactivateImageController
   * @description
   * This controller is use for updating an image.
   */
  function DeactivateImageController(
    $scope
  ) {
    var ctrl = this;

    ctrl.imageStatusOptions = [
      { label: gettext('Active'), value: 'active' },
      { label: gettext('Deactivated'), value: 'deactivated' }
    ];

    $scope.imagePromise.then(init);

    ///////////////////////////

    function init(response) {
      $scope.stepModels.deactivateForm = ctrl.image = response.data;
      ctrl.image.status = ctrl.image.status || 'active'; // initial status
    }

 

 
  } // end of controller

})();
