
    function updateImage(image) {
      if(image.status === "deactivated"){
        apiService.post('/images/{image_id}/actions/deactivate')
      }
      return apiService.patch('/api/glance/images/' + image.id + '/', image)
        .catch(function onError() {
          toastService.add('error', gettext('Unable to update the image.'));
        });
    }
 
