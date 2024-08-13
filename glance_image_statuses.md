Here's a markdown-formatted summary of the different image statuses highlighted in the document:

| Status | Description |
|--------|-------------|
| `queued` | The Image service reserved an image ID for the image in the catalog but has not yet uploaded any image data. |
| `saving` | The Image service is in the process of saving the raw data for the image into the backing store. |
| `active` | The image is active and ready for consumption in the Image service. |
| `killed` | An image data upload error occurred. |
| `deleted` | The Image service retains information about the image but the image is no longer available for use. |
| `pending_delete` | Similar to the `deleted` status. An image in this state is not recoverable. |
| `deactivated` | The image data is not available for use. |
| `uploading` | Data has been staged as part of the interoperable image import process. It is not yet available for use. (Since Image API 2.6) |
| `importing` | The image data is being processed as part of the interoperable image import process, but is not yet available for use. (Since Image API 2.6) |

These statuses represent the different stages an image can be in throughout its lifecycle in the OpenStack Image service. They indicate whether an image is ready for use, in the process of being uploaded or imported, or has been removed or encountered errors.
