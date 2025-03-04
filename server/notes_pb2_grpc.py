# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import notes_pb2 as notes__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in notes_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NoteServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNote = channel.unary_unary(
                '/notes.NoteService/CreateNote',
                request_serializer=notes__pb2.CreateNoteRequest.SerializeToString,
                response_deserializer=notes__pb2.NoteResponse.FromString,
                _registered_method=True)
        self.GetNote = channel.unary_unary(
                '/notes.NoteService/GetNote',
                request_serializer=notes__pb2.GetNoteRequest.SerializeToString,
                response_deserializer=notes__pb2.NoteResponse.FromString,
                _registered_method=True)
        self.ListNotes = channel.unary_unary(
                '/notes.NoteService/ListNotes',
                request_serializer=notes__pb2.ListNotesRequest.SerializeToString,
                response_deserializer=notes__pb2.ListNotesResponse.FromString,
                _registered_method=True)
        self.UpdateNote = channel.unary_unary(
                '/notes.NoteService/UpdateNote',
                request_serializer=notes__pb2.UpdateNoteRequest.SerializeToString,
                response_deserializer=notes__pb2.NoteResponse.FromString,
                _registered_method=True)
        self.DeleteNote = channel.unary_unary(
                '/notes.NoteService/DeleteNote',
                request_serializer=notes__pb2.DeleteNoteRequest.SerializeToString,
                response_deserializer=notes__pb2.DeleteNoteResponse.FromString,
                _registered_method=True)


class NoteServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NoteServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNote': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNote,
                    request_deserializer=notes__pb2.CreateNoteRequest.FromString,
                    response_serializer=notes__pb2.NoteResponse.SerializeToString,
            ),
            'GetNote': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNote,
                    request_deserializer=notes__pb2.GetNoteRequest.FromString,
                    response_serializer=notes__pb2.NoteResponse.SerializeToString,
            ),
            'ListNotes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNotes,
                    request_deserializer=notes__pb2.ListNotesRequest.FromString,
                    response_serializer=notes__pb2.ListNotesResponse.SerializeToString,
            ),
            'UpdateNote': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNote,
                    request_deserializer=notes__pb2.UpdateNoteRequest.FromString,
                    response_serializer=notes__pb2.NoteResponse.SerializeToString,
            ),
            'DeleteNote': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNote,
                    request_deserializer=notes__pb2.DeleteNoteRequest.FromString,
                    response_serializer=notes__pb2.DeleteNoteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notes.NoteService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('notes.NoteService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NoteService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes.NoteService/CreateNote',
            notes__pb2.CreateNoteRequest.SerializeToString,
            notes__pb2.NoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes.NoteService/GetNote',
            notes__pb2.GetNoteRequest.SerializeToString,
            notes__pb2.NoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListNotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes.NoteService/ListNotes',
            notes__pb2.ListNotesRequest.SerializeToString,
            notes__pb2.ListNotesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes.NoteService/UpdateNote',
            notes__pb2.UpdateNoteRequest.SerializeToString,
            notes__pb2.NoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes.NoteService/DeleteNote',
            notes__pb2.DeleteNoteRequest.SerializeToString,
            notes__pb2.DeleteNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
