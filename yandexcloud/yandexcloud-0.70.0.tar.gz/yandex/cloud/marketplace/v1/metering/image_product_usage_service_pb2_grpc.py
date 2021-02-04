# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.marketplace.v1.metering import image_product_usage_service_pb2 as yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2


class ImageProductUsageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Write = channel.unary_unary(
                '/yandex.cloud.marketplace.v1.metering.ImageProductUsageService/Write',
                request_serializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageResponse.FromString,
                )


class ImageProductUsageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Write(self, request, context):
        """Writes image product's usage (authenticated by user's service account)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageProductUsageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.marketplace.v1.metering.ImageProductUsageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageProductUsageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.marketplace.v1.metering.ImageProductUsageService/Write',
            yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageRequest.SerializeToString,
            yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
