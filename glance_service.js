// an unhandled rejection error and a 404 since it's looking for a page called 'deactivate'
    function updateImage(image) {
      if(image.status === "deactivated"){
        apiService.post('/images/{image_id}/actions/deactivate')
      }
      return apiService.patch('/api/glance/images/' + image.id + '/', image)
        .catch(function onError() {
          toastService.add('error', gettext('Unable to update the image.'));
        });
    }
 
