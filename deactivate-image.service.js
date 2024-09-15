/**
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use self file except in compliance with the License. You may obtain
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

(function() {
  'use strict';

  angular
    .module('horizon.app.core.images')
    .factory('horizon.app.core.images.actions.deactivate-image.service', deactivateImageService);

  deactivateImageService.$inject = [
    '$q',
    'horizon.app.core.openstack-service-api.glance',
    'horizon.app.core.openstack-service-api.policy',
    'horizon.framework.util.actions.action-result.service',
    'horizon.framework.util.i18n.gettext',
    'horizon.framework.util.q.extensions',
    'horizon.framework.widgets.modal.simpleModalService',
    'horizon.framework.widgets.toast.service',
    'horizon.app.core.images.resourceType'
  ];

  /*
   * @ngdoc factory
   * @name horizon.app.core.images.actions.deactivate-image.service
   *
   * @Description
   * Brings up the deactivate image confirmation modal dialog.

   * On submit, deactivate the given image
   * On cancel, do nothing.
   */
  function deactivateImageService(
    $q,
    glance,
    policy,
    actionResultService,
    gettext,
    $qExtensions,
    simpleModal,
    toast,
    imageResourceType
  ) {
    var notAllowedMessage = gettext("You are not allowed to deactivate image: %s");

    var service = {
      allowed: allowed,
      perform: perform
    };

    return service;

    //////////////

    function perform() {      
      var context = { };      
      context.labels = labelize();
      context.deactivateEntity = deactivateImage;

      return $q.all(checkPermission).then(afterCheck);

      function checkPermission(image) {
        return {promise: allowed(image), context: image};
      }

      function afterCheck(result) {
        var outcome = $q.reject().catch(angular.noop);  // Reject the promise by default
        if (result.fail) {
          toast.add('error', getMessage(notAllowedMessage, result.fail));
          outcome = $q.reject(result.fail).catch(angular.noop);
        }
        if (result.pass) {
          outcome = simpleModal.open(scope, result.pass, context).then(onDeactivateImageSuccess, onDeactivateImageFail);
        }
        return outcome;
      }
    }

    function allowed(image) {
      return $q.all([        
        policy.ifAllowed({ rules: [['image', 'deactivate']] }),
        notDeactivated(image)
      ]);
    }

    function onDeactivateImageSuccess() {
      toast.add('success', interpolate(context.labels.success, [image.name]));
      return actionResultService.getActionResult()
        .updated(imageResourceType, item.id)
        .result;
    }

    function onDeactivateImageFail() {
      toast.add('error', interpolate(context.labels.error, [image.name]));
      return actionResultService.getActionResult()
        .failed(imageResourceType, item.id)
        .result;
    }

    function labelize() {
      return {
        title: gettext('Confirm Deactivate Image'),
        message: gettext('You have selected "%s". A deactivated image is not downloadable.'),
        submit: gettext('Deactivate Image'),
        success: gettext('Deactivated Image: %s.'),
        error: gettext('Unable to deactivate Image: %s.')
      };
    }

    function notDeactivated(image) {
      return $qExtensions.booleanAsPromise(image.status !== 'deactivated');
    }

    function deactivateImage(image) {
      return glance.deactivateImage(image, true);
    }

    function getMessage(message, image) {
      return interpolate(message, [image.name]);
    }
  }
})();
